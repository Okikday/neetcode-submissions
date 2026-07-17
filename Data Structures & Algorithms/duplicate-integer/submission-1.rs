impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut dup_set = HashSet::new();

        for num in nums{

            if dup_set.contains(&num){
                return true;
            }
            dup_set.insert(num);
        }
        false
    }
}
