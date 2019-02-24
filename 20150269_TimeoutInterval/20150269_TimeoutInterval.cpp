#include <iostream>

#define a 0.875
#define b 0.75

int SampleRTT(int k);
double EstimatedRTT(int k);
double DevRTT(int k);
double TimeoutInterval(int k);

int main(void)
{	
	std::cout << "TimeoutInterval[11] = " << TimeoutInterval(11) << std::endl;
	std::cout << "TimeoutInterval[20] = " << TimeoutInterval(20) << std::endl;
	std::cout << "EstimatedRTT[11] = " << EstimatedRTT(11) << std::endl;
	std::cout << "EstimatedRTT[20] = " << EstimatedRTT(20) << std::endl;

	return 0;
}

int SampleRTT(int k) 
{
	if ((k >= 1) && (k <= 10))
		return 1;
	else if (k > 10)
		return 3;
}

double EstimatedRTT(int k)
{
	if (k == 1)
		return SampleRTT(k);
	else
		return (a*EstimatedRTT(k - 1)) + ((1 - a)*SampleRTT(k));
}

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
