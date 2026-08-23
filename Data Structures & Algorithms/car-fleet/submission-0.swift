class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        var pairs: [(Int, Int)] = []
        for i in 0..<position.count{
            pairs.append((position[i], speed[i]))
        }
        pairs.sort{$0.0 > $1.0}

        var stack: [Double] = []
        
        for (pos, spd) in pairs{
            stack.append(Double(target - pos) / Double(spd))

            if stack.count >= 2 && stack.last! <= stack[stack.count - 2]{
                stack.removeLast()
            }
        }
        return stack.count
    }
}
