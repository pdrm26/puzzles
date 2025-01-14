export default class Solution {
  cleanerData(text: string): string {
    const alphanumericChars =
      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    let cleanedString = "";

    for (let i of text) {
      if (alphanumericChars.includes(i)) {
        cleanedString += i.toLowerCase();
      }
    }

    return cleanedString;
  }

  isPalindrome(s: string): boolean {
    let cleanedString = this.cleanerData(s);
    let startPointer = 0;
    let endPointer = cleanedString.length - 1;

    while (startPointer < endPointer) {
      if (cleanedString.at(startPointer) == cleanedString.at(endPointer)) {
        startPointer += 1;
        endPointer -= 1;
        continue;
      }

      return false;
    }

    return true;
  }
}

const solution = new Solution();
let s = "A man, a plan, a canal: Panama";
s = "doggods";

const result = solution.isPalindrome(s);
console.log(result);
