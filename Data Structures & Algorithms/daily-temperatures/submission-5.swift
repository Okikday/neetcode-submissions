class Solution{
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        var res: [Int] = Array(repeating: 0, count: temperatures.count)
        var stack: [Int] = []

        for i in 0...(temperatures.count-1){
            while !stack.isEmpty && temperatures[i] > temperatures[stack.last!]{
                res[stack.last!] = i - stack.removeLast()
            }
            stack.append(i)
        }
        return res
    }
}