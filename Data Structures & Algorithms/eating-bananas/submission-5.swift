class Solution{
 
    func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {
    let n = piles.count
    if n == 1 && piles.first! == h{
        return 1
    }
    let sortedPiles: [Int] = piles.sorted()

    let optVal = n == 1 ? piles.first! : sortedPiles[performSearch(sortedPiles, h)]
    if optVal <= 1{
        return 1
    }
    var lo = 1
    var hi = optVal - 1
    var newOpt = optVal
    while lo <= hi{
        let mid = lo + (hi - lo) / 2
        var spd: Int = 0
        for i in 0..<n{
            spd += (sortedPiles[i] / mid) + ((sortedPiles[i] % mid) > 0 ? 1 : 0)
        }
        if mid < newOpt  && spd <= h{
            newOpt = mid
            hi = mid - 1
        }
        else{
            lo = mid + 1
        }
        
    }

    
    return newOpt
    }

    func performSearch(_ piles: [Int], _ h: Int) -> Int{
    let n = piles.count
    var lo = 0
    var hi = n - 1
    var opt: Int = hi
    // opt = 4
    // [1, 2, 3, 4]
    while lo <= hi{
        let mid = lo + (hi - lo) / 2
        var spd: Int = 0
        let tar = piles[mid]
        for i in 0..<n{
            spd += (piles[i] / tar) + ((piles[i] % tar) > 0 ? 1 : 0)
        }
        if tar < piles[opt] && spd <= h{
            opt = mid
            hi = mid - 1
        }else{
            lo = mid + 1
        }
    }
    return opt
    }


}