module Tree where
import Data.char

data Tree a = Empty | Node a (Tree a) (Tree a)

instance
