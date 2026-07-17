impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if t.len() != s.len() {
            return false;
        }

        let mut s_map = HashMap::new();
        let mut t_map = HashMap::new();

        for (s, t) in s.bytes().zip(t.bytes()) {
            *s_map.entry(s).or_insert(0) += 1;
            *t_map.entry(t).or_insert(0) += 1;
        }

        s_map == t_map
    }
}