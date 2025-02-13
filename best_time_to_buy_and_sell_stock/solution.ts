function maxProfit(prices: number[]): number {
  let maxProfit = 0;
  let minPrice = Infinity;

  for (let price of prices) {
    if (price < minPrice) {
      minPrice = price;
    }

    const thisProfit = price - minPrice;
    if (thisProfit > maxProfit) {
      maxProfit = thisProfit;
    }
  }

  return maxProfit;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
console.log(maxProfit([2, 4, 1]));
