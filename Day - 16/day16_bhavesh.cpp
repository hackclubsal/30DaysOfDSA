#include <iostream>
#include <stdlib.h>
#include <limits.h>
using namespace std;
 
void TugofWarRecur(int* array, int n, bool* current_elements, int selected_elements_count,bool* solution, int* min_diff, int sum, int current_sum, int current_position)
{
    
    if (current_position == n)
    {
        return;
    }
    if ((n/2 - selected_elements_count) > (n - current_position))
    {
        return;
    }
 
    TugofWarRecur(array, n, current_elements, selected_elements_count,solution, min_diff, sum, current_sum, current_position+1);
 
    selected_elements_count++;
    current_sum = current_sum + array[current_position];
    current_elements[current_position] = true;
    if (selected_elements_count == n/2)
    {
        if (abs(sum/2 - current_sum) < *min_diff)
        {
            *min_diff = abs(sum/2 - current_sum);
            for (int i = 0; i<n; i++)
            {
                solution[i] = current_elements[i];
            }
        }
    }
    else
    {
        TugofWarRecur(array, n, current_elements, selected_elements_count, solution, min_diff, sum, current_sum, current_position+1);
    }
    current_elements[current_position] = false;
}
 
void TugOfWar(int *array, int n)
{
    bool* current_elements = new bool[n];
    bool* solution = new bool[n];
    int min_diff = INT_MAX;
    int sum = 0;
    for (int i=0; i<n; i++)
    {
        sum =sum + array[i];
        current_elements[i] =  solution[i] = false;
    }
    TugofWarRecur(array, n, current_elements, 0, solution, &min_diff, sum, 0, 0);
    for (int i=0; i<n; i++)
    {
        if(solution[i] == true)
        {
            cout << array[i] << " ";
        }
    }
    cout<<endl;
    for (int i=0; i<n; i++)
    {
        if(solution[i] == false)
        {
            cout << array[i] << " ";
        }
    }
}
 

int main()
{
    int n;
    cin>>n;
    int input_array[n];
    for(int i=0;i<n;i++)
    {
        cin>>input_array[i];
    }
    TugOfWar(input_array,n);
    return 0;
}
