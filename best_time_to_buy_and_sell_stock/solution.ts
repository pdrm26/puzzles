function maxProfit(prices: number[]): number {
  let maxProfit = 0;

  for (let buy = 0; buy < prices.length; buy++) {
    for (let sell = buy + 1; sell < prices.length; sell++) {
      let thisProfit = prices[sell] - prices[buy];

      if (thisProfit > maxProfit) {
        maxProfit = thisProfit;
      }
    }
  }

  return maxProfit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
console.log(maxProfit([2, 4, 1]));
