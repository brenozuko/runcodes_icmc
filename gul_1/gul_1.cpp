#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{

		int n, T[1000], S[1000];
		int res[1000];

		cin >> n;

		for (int i = 0; i < n; i++)
			scanf("%d%d", &T[i], &S[i]), res[i] = i;

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n - 1; j++)
			{

				if (T[res[j]] * S[res[j + 1]] > S[res[j]] * T[res[j + 1]])
					swap(res[j], res[j + 1]);

				else if (T[res[j]] * S[res[j + 1]] == S[res[j]] * T[res[j + 1]] && res[j] > res[j + 1])
					swap(res[j], res[j + 1]);
			}
		}

		cout << res[0] + 1;

		for (int i = 1; i < n; i++)
			cout << " " << res[i] + 1;

		putchar('\n');

		if (t != 0)
			putchar('\n');
	}
	return 0;
}
