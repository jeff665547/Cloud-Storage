/* ifndef, define, endif 的用法 */
/* #if, #ifdef, #ifndef 常常在 C 語言或是C++程式裡看到,
就是讓 compiler 去辨識哪一段程式要, 
哪一段程式不要。這個是為了怕重覆 include 的狀況發生,
假如 a.h 裡 include 了 b.h 
而 main.cpp 這個檔裡 include a.h 跟 b.h, 
如果沒有#ifndef 來攔住, 
跟一個#define來標示出已經include 過了, 
那麼content裡面的東西都會重複定義喔, 
重複定義當然沒什麼大不了的, 
可是compiler很笨, 它只分得出來重複定義, 
分不出來值都是一樣的, 
所以只好這樣子讓compiler來辨別囉. */

/* 為了避免聲明衝突，
會把頭文件的內容都放在#ifndef和#endif中。
/* 不管你的header文件會不會被多個文件引用，
你都要加上這個。一般格式是這樣的: */
// #ifndef <標識>
// #define <標識>
// ......
// ......
// #endif

// <標識>在理論上來說可以是自由命名的，
// 但每個頭文件的這個「標識」都應該是唯一的。
// 標識的命名規則一般是頭文件名全大寫，前後加下劃線，
// 並把文件名中的「.」也變成下劃線，如：stdio.h 
// ifndef _STDIO_H_ 
// #define _STDIO_H_ 
// ...... 
// #endif 

#ifndef HELLO_H
#define HELLO_H

void hello();  // hello 函式的宣告

#endif
