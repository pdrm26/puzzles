package main

func majorityElement(nums []int) int {
	m := map[int]int{}

	for _, num := range nums {
		m[num]++
	}

	for key, count := range m {
		if count > len(nums)/2 {
			return key
		}
	}

	return -1
}

func main() {
	majorityElement([]int{2, 2, 1, 1, 1, 2, 2})
	majorityElement([]int{3, 2, 3})
}
