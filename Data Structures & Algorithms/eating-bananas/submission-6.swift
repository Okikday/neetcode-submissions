class Solution {

func minEatingSpeed(_ piles: [Int], _ h: Int) -> Int {

    var lo = 1, hi = piles.max()! - 1, opt = hi + 1
    while lo <= hi{
        let mid = (lo + hi) / 2
        var spd: Int = 0
        for pile in piles{
            spd += (pile / mid) + ((pile % mid) > 0 ? 1 : 0)
        }
        if mid < opt && spd <= h{
            opt = mid
            hi = mid - 1
        }
        else{
            lo = mid + 1
        }
       
    }
    return opt
}


}
