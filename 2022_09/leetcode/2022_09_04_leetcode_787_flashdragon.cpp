#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<map>
using namespace std;
typedef long long ll;
set<string>s;
void go(string a, int n);
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t, test_case = 0;
	cin >> t;
	for (test_case = 0; test_case < t; test_case++)
	{
		string Answer = "";
		int n, m;
		cin >> n >> m;
		string a, b;
		cin >> a >> b;
		if (n < m)
			Answer = "NO";
		else if (n == m && a == b)
			Answer = "YES";
		else if (n == m && a != b)
			Answer = "NO";
		else
		{
			
		}
		cout << "Case #" << test_case + 1 << endl;
		cout << Answer << endl;
	}
}

void go(string a, int n)
{
	if (n == 0)
	{
		s.insert(a);
		return;
	}
	string temp = a;
	int idx = temp.find("a");
	if (idx != string::npos)
	{
		go(temp.erase(idx), n - 1);
	}
	string temp = a;
	int idx = temp.find("b");
	if (idx != string::npos)
	{
		go(temp.erase(idx), n - 1);
	}

}
