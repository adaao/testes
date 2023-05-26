main :: IO ()
main = countTo 1000000000

countTo :: Int -> IO ()
countTo n = go 0
  where
    go :: Int -> IO ()
    go i
      | i < n = go (i + 1)
      | i == n = putStrLn $ show i
      | otherwise = return ()