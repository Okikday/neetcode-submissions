impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_map = HashMap::new();
        
        for letter in s.chars(){
            *s_map.entry(letter).or_insert(0) += 1;
        }

        for letter in t.chars(){
            if let Some(count) = s_map.get_mut(&letter){
                if *count == 1{
                    s_map.remove(&letter);
                }else{
                    *count -= 1;
                }
                continue;
            }
            return false
        }

        s_map.is_empty()
    }
}
