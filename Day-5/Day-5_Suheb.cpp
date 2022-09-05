#include <iostream>
using namespace std;

void search(int nums[], int start, int end)
{
	if (start > end)
		return;

	if (start == end) {
		cout << nums[start];
		return;
	}

	int mid = (start + end) / 2;

	if (mid % 2 == 0) {
		if (nums[mid] == nums[mid + 1])
			search(nums, mid + 2, end);
		else
			search(nums, start, mid);
	}

	else {
		if (nums[mid] == nums[mid - 1])
			search(nums, mid + 1, end);
		else
			search(nums, start, mid - 1);
	}
}

int main()
{
	int nums[] = {1, 1, 2, 3, 3, 4, 4};
	int len = sizeof(nums) / sizeof(nums[0]);

	search(nums, 0, len - 1);

	return 0;
}

