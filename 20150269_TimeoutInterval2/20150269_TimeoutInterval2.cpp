#include <iostream>

#define a 0.875
#define b 0.75

int SampleRTT(int k);
double EstimatedRTT(int k);
double DevRTT(int k);
double TimeoutInterval(int k);

int main(void)
{
	int i = 990;

	std::cout << "TimeoutInterval[991] = " << TimeoutInterval(991) << std::endl;
	std::cout << "TimeoutInterval[1000] = " << TimeoutInterval(1000) << std::endl;
	std::cout << "EstimatedRTT[991] = " << EstimatedRTT(991) << std::endl;
	std::cout << "EstimatedRTT[1000] = " << EstimatedRTT(1000) << std::endl;

	while (i<1100)
	{
		i++;
		std::cout << i << " " << TimeoutInterval(i) << std::endl;
	}

	getchar();
	return 0;
}

int SampleRTT(int k)
{
	if ((k >= 1) && (k <= 990))
		return 1;
	else if (k > 990)
		return 3;
}

double EstimatedRTT(int k)
{
	if (k == 1)
		return SampleRTT(k);
	else
		return (a*EstimatedRTT(k - 1)) + ((1 - a)*SampleRTT(k));
}

/*double EstimatedRTT(int k)
{
	int sum = 0;

	for (int i = 1; i <= k; i++)
		sum += SampleRTT(i);

	return (double)sum / k;
}*/

double DevRTT(int k)
{
	double result;

	if (k == 1)
		return 0;
	else
	{
		if ((SampleRTT(k) - EstimatedRTT(k)) >= 0)
			result = SampleRTT(k) - EstimatedRTT(k);
		else if ((EstimatedRTT(k) - SampleRTT(k)) > 0)
			result = EstimatedRTT(k) - SampleRTT(k);

		return (b*DevRTT(k - 1)) + ((1 - b)*result);
	}
}

double TimeoutInterval(int k)
{
	return EstimatedRTT(k) + (4 * DevRTT(k));
}