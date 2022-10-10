#include </Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers/pyconfig.h>
#include <boost/python.hpp>
// /usr/local/Cellar/boost/1.78.0/include/
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/range/algorithm.hpp>
#include <iostream>
#include <boost/algorithm/algorithm.hpp>
#include </Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers/Python.h>
using namespace boost;
using namespace boost::algorithm;
using namespace boost::numeric::ublas;


vector<int> clipVec(vector<int> id, vector<int> seq, vector<int> event) { 

  // int uid = boost::python::len(boost::unique(boost::range::sort(id)));

  int uid = boost::unique(boost::sort(id)).size();

  vector<int> last(uid);
  // * converts iterator to int?
  int maxperiod = *boost::range::max_element(seq);
  int xid;
  
  for(int i=0; i<id.size(); ++i) {
    
    if (seq[i] == 1) {
      xid = id[i] - 1;
    }
    
    if (last[xid] == 0) {
      
      if (seq[i] < maxperiod) {
        if (event[i] == 1) last[xid] = seq[i];
      } else last[xid] = seq[i];
      
    }
    
  }
  std::cout<<last;
  std::cout<<"<<< Here is last";
  return last;
}
int main()
{
  using namespace boost;
  using namespace boost::algorithm;
  using namespace boost::numeric::ublas;
  
  vector<int> a (3);
  for (unsigned i = 0; i < a.size (); ++ i)
    a (i) = i;
  std::cout<<a;
  std::cout<<"<<< variable a\n";
  vector<int> b (3);
  for (unsigned i = 0; i < b.size (); ++ i)
    b (i) = i;
  vector<int> c (3);
  for (unsigned i = 0; i < c.size (); ++ i)
    c (i) = i;

  clipVec(a, b, c);

}