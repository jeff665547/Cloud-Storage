// Selection sort (選擇排序)
// 將要排序的對象分作兩部份，一個是已排序的，一個是未排序的。
// 如果排序是由小而大，從後端未排序部份選擇一個最小值，並放入前端已排序部份的最後一個。
//
// e.g.: 排序前：70 80 31 37 10 1 48 60 33 80
// 在下面的範例中[ ]內代表是已排序的對象。
// 1. [1] 80 31 37 10 70 48 60 33 80；選出最小值1
// 2. [1 10] 31 37 80 70 48 60 33 80；選出最小值10
// 3. [1 10 31] 37 80 70 48 60 33 80；選出最小值31
// 4. [1 10 31 33] 80 70 48 60 37 80 ......
// 5. [1 10 31 33 37] 70 48 60 80 80 ......
// 6. [1 10 31 33 37 48] 70 60 80 80 ......
// 7. [1 10 31 33 37 48 60] 70 80 80 ......
// 8. [1 10 31 33 37 48 60 70] 80 80 ......
// 9. [1 10 31 33 37 48 60 70 80] 80 ......




// Insertion sort (插入排序)
// 將要排序的對象分作兩部份，一個是已排序的，一個是未排序的。
// 每次從後端未排序部份取得最前端的值，然後插入前端已排序部份的適當位置。
// 
// e.g.: 排序前：92 77 67 8 6 84 55 85 43 67
// 在下面的範例中[ ]內代表是已排序的對象。
// 1. [77 92] 67 8 6 84 55 85 43 67；將77插入92前
// 2. [67 77 92] 8 6 84 55 85 43 67；將67插入77前
// 3. [8 67 77 92] 6 84 55 85 43 67；將8插入67前
// 4. [6 8 67 77 92] 84 55 85 43 67；將6插入8前
// 5. [6 8 67 77 84 92] 55 85 43 67；將84插入92前
// 6. [6 8 55 67 77 84 92] 85 43 67；將55插入67前
// 7. [6 8 55 67 77 84 85 92] 43 67 ......
// 8. [6 8 43 55 67 77 84 85 92] 67 ......
// 9. [6 8 43 55 67 67 77 84 85 92] ......




// Bubble sort (氣泡排序)
// 將要排序的對象分作兩部份，一個是已排序的，一個是未排序的。
// 排序時若是從小到大，最大元素會如同氣泡一樣移至右端，
// 其利用比較相鄰元素的方式，將較大元素交換至右端，
// 所以較大的元素會不斷往右移動，直到適當的位置為止。
// 
// e.g.: 排序前：95 27 90 49 80 58 6 9 18 50
// 在下面的範例中[ ]內代表是已排序的對象。
// 27 90 49 80 58 6 9 18 50 [95]；95浮出
// 27 49 80 58 6 9 18 50 [90 95]；90浮出
// 27 49 58 6 9 18 50 [80 90 95]；80浮出
// 27 49 6 9 18 50 [58 80 90 95] ......
// 27 6 9 18 49 [50 58 80 90 95] ......
// 6 9 18 27 [49 50 58 80 90 95] ......
// 6 9 18 [27 49 50 58 80 90 95] ......
// 6 9 [18 27 49 50 58 80 90 95] ......
// 6 [9 18 27 49 50 58 80 90 95] ...... 
// [6 9 18 27 49 50 58 80 90 95] ...... 


