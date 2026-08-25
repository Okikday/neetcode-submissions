
typealias TimeVal = (time: Int, val: String)
class TimeMap {
    var timeDict: [String:[TimeVal]] = [:]
    init() {

    }

    func set(_ key: String, _ value: String, _ timestamp: Int) {
        if timeDict[key] == nil{
            timeDict[key] = [TimeVal]()
        }
        
        timeDict[key]!.insert((timestamp, value), at: insertionBinarySearch(timeDict[key]!, timestamp))
    }
    
    func insertionBinarySearch(_ arr: [TimeVal], _ timestamp: Int) -> Int{
        var lo = 0, hi = arr.count
        
        while lo < hi{
            let mid = lo + (hi - lo) / 2
            if arr[mid].time < timestamp{
                lo = mid + 1
            }else{
                hi = mid
            }
        }
        return lo
    }

    func get(_ key: String, _ timestamp: Int) -> String {
        if timeDict[key] == nil || timeDict[key]!.isEmpty{
             return ""
        }
        
        var lo = 0, hi = timeDict[key]!.count - 1, opt = -1
        
        while lo <= hi{
            let mid = lo + (hi - lo) / 2
            if timeDict[key]![mid].time <= timestamp{
                opt = mid
                lo = mid + 1
            }else{
                hi = mid - 1
            }
        }
        return opt == -1  ? "" : timeDict[key]![opt].val
    }
}
