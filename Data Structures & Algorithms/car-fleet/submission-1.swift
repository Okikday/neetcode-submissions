class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        var pairs: [(Int, Int)] = []
        for i in 0..<position.count{
            pairs.append((position[i], speed[i]))
        }
        pairs.sort{$0.0 > $1.0}

        var prevTime = Double(target - pairs[0].0) / Double(pairs[0].1)
        var count = 1
        
        for (pos, spd) in pairs[1...]{
            let currTime = Double(target - pos) / Double(spd)
            if currTime > prevTime{
                count += 1
                prevTime = currTime
            }
        }
        return count
    }
}
