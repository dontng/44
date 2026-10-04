import importlib.util
import tempfile
import unittest
from pathlib import Path
from datetime import date,timedelta
ROOT=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('review',ROOT/'tools/review.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def event(day,result='independent',item='q:2011-01',mode='original',**extra):
 return dict(id=day+result,item=item,date=day,created_at=day,result=result,mode=mode,note='test evidence',**extra)

class ReviewTest(unittest.TestCase):
 def test_catalog_deduplicates_cross_line_questions(self):
  c=m.catalog();self.assertEqual(len(c),895)
  self.assertGreater(len(c['q:2014-03']['lines']),1)
  self.assertEqual(sum(k=='q:2014-03' for k in c),1)
  for v in c.values():
   for key in ('path','answer','review'):self.assertTrue((ROOT/v[key].split('#')[0]).exists(),v)
 def test_no_records_means_no_queue(self):
  self.assertEqual(m.states([],date.today()),{})
  self.assertEqual(m.choose(m.catalog(),{},date.today()),([],0,0))
 def test_append_preserves_existing_attempt(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);c=m.catalog()
   first=m.append_event(p,c,'q:2011-01','failed','只能列前三轮')
   f=next(p.glob('*.json'));original=f.read_bytes()
   m.append_event(p,c,'q:2011-01','prompted','提示后会求和')
   self.assertEqual(f.read_bytes(),original);self.assertEqual(len(m.read_events(p)),2)
   with self.assertRaises(ValueError):m.append_event(p,c,'q:2011-01','independent','',when=date.today())
   with self.assertRaises(ValueError):m.append_event(p,c,'q:2011-01','independent','future',when=date.today()+timedelta(days=1))
 def test_same_day_and_early_repetition_do_not_advance(self):
  rows=[event('2026-01-01'),event('2026-01-01'),event('2026-01-02')]
  s=m.states(rows,date(2026,1,2))['q:2011-01'];self.assertEqual(s['due'],'2026-01-05')
  rows.append(event('2026-01-03'))
  self.assertEqual(m.states(rows,date(2026,1,3))['q:2011-01']['due'],'2026-01-05')
 def test_failure_shortens_and_same_day_correction_is_not_independent(self):
  rows=[event('2026-01-01'),event('2026-01-02'),event('2026-01-05'),event('2026-01-12','failed'),event('2026-01-12')]
  s=m.states(rows,date(2026,1,12))['q:2011-01'];self.assertEqual(s['due'],'2026-01-13');self.assertEqual(s['result'],'failed')
 def test_transfer_requires_real_prior_evidence_and_only_affects_named_item(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);c=m.catalog();old=date.today()-timedelta(days=7)
   with self.assertRaises(ValueError):m.append_event(p,c,'q:2012-01','independent','new',mode='transfer',reinforces='q:2011-01',transfer_note='same summation')
   m.append_event(p,c,'q:2011-01','independent','sum trace',when=old)
   m.append_event(p,c,'q:2012-01','independent','new condition',mode='transfer',reinforces='q:2011-01',transfer_note='used sum rather than product')
   s=m.states(m.read_events(p),date.today());self.assertEqual(set(s),{'q:2011-01','q:2012-01'});self.assertEqual(s['q:2011-01']['transfer_days'],1)
 def test_queue_respects_time_limit_and_does_not_split_written(self):
  c=m.catalog();rows=[event('2026-01-01','failed','q:2009-42'),event('2026-01-01',item='q:2011-01')]
  s=m.states(rows,date(2026,1,10));before=dict(s)
  selected,waiting,cost=m.choose(c,s,date(2026,1,10),minutes=10)
  self.assertEqual(selected,['q:2011-01']);self.assertEqual(waiting,1);self.assertEqual(s,before)
  selected,_,cost=m.choose(c,s,date(2026,1,10),limit=1,minutes=25)
  self.assertEqual(selected,['q:2009-42']);self.assertEqual(cost,20)

if __name__=='__main__':unittest.main()
