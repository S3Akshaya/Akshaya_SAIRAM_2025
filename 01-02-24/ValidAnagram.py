''' 
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
  '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val={}
        for i in s:
            if i not in val:
                val[i]=1
            else:
                val[i]+=1
        for i in t:
            if i not in val:
                return False
            else:
                val[i]-=1
        for j in val.values():
            if j!=0:
                return False
        return True
