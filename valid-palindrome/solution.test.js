import { describe, test } from "node:test";
import assert from "node:assert/strict";
import Solution from "./solution.ts";

describe("cleanerData function", async () => {
  const solution = new Solution();

  await test("should remove non-alphanumeric characters", () => {
    assert.equal(solution.cleanerData("Hello, World!"), "helloworld");
    assert.equal(
      solution.cleanerData("A man, a plan, a canal: Panama"),
      "amanaplanacanalpanama"
    );
    assert.equal(solution.cleanerData("123 ABC!"), "123abc");
  });
});

describe("isPalindrome function", async () => {
  const solution = new Solution();

  await test("Should return true for palindromic strings", () => {
    assert.strictEqual(
      solution.isPalindrome("A man, a plan, a canal: Panama"),
      true
    );
    assert.strictEqual(solution.isPalindrome("doggods"), false);
    assert.strictEqual(solution.isPalindrome("No lemon, no melon"), true);
  });
});
