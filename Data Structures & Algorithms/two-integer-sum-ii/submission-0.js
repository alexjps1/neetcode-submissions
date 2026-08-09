class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
    let difference;
    let j = numbers.length - 1;
    for (let i = 0; i < j ; i++) {
        difference = target - numbers[i];
        while (numbers[j-1] >= difference && j-1 > i) {
            j--;
        }
        if (numbers[i] + numbers[j] === target) {
            return [i+1, j+1];
        }
    }
};
}
