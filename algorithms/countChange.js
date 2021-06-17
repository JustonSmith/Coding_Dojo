// Generate Coin Change
// Change is inevitable (especially when breaking a twenty).

// Make generateCoinChange(cents).
// Accept a number of American cents, compute and print how to represent that amount with smallest number of coins. Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). Return the optimal configuration of coins in an object.

// Example output, given generateCoinChange(94), return
// { quarters:3, dimes:1, nickels:1, pennies:4}

function generateCoinChange(coins, amount){
    var finalResult = FindMinCount(coins, 0, 0, amount, 0, amount + 1)
    function FindMinCount(coins, i, currentSum, amount, count, result){
        // console.log(coins, i, currentSum, amount, count, result)
        if (amount == 0){
            return 0
        }

        if (currentSum > amount){
            return result
        }

        if(currentSum == amount){
            // console.log(result, count)
            result = Math.min(count, result)
            return result
        }
        
        if( i <= coins.length - 1){
            count ++
            result = FindMyCount(coins, i, currentSum + coins[i], amount, count, result)

            count --
            result = FindMinCount(coins, i+1, currentSum, amount, count, result)
        }
        return result
    }

    if (finalResult == initialResult){
        return - 1
        }
    else{
        return finalResult
    }
}

console.log(coinChange([1, 2, 5], 11))






function generateCoinChange(coins, sum, numCoins) {
	if (numCoins === undefined) {numCoins = coins.length;}
	if (sum == 0) {return 1;}
	if (sum < 0) {return 0;}
	if (numCoins <= 0 && sum > 0) {return 0;}
	return generateCoinChange(coins, sum, numCoins - 1) + generateCoinChange(coins, sum - coins[numCoins - 1], numCoins);
}

console.log(generateCoinChange([1,2,3], 4));

