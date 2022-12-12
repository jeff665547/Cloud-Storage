<?php
	/* 
	 * isset() 可以檢查變數是否已設定值，
	 		   若變數值為 NULL，傳回 false，
	 		   否則傳回 true
	 *
	 * unset() 可以把變數值設為 NULL
	 */
	/**** 範例 ****/
	/*
		$a = 1;
		if(isset($a))
			echo '$a is set!<br>';
		if(!isset($b))
			echo '$b is not set!<br>';

		unset($a);
		if(!isset($a))
			echo '$a is not set now!<br>';
	*/

	/*
	 * ---------- 數學函式 ----------
	 *
	 * abs(x)   傳回 x 的絕對值
	 * ceil(x)  傳回大於等於 x 最小的整數 
	 * floor(x) 傳回小於等於 x 最大的整數
	 * round(x[, precision]) 四捨五入，precision 可以指定四捨五入至哪一小數位
	 *
	 * pow(base, exp) 取 base 的 exp 次方
	 * sqrt(x) 取平方根
	 *
	 * max(x1, x2[, x3, ...]) 取最大值
	 * max(arr1) 取陣列中最大值 
	 *
	 * min(x1, x2[, x3, ...]) 取最小值
	 * min(arr1) 取陣列中最小值
	 *
	 * rand([min, max]) 傳回 min 和 max 之間的亂數，若未設則是 0 到 RAND_MAX 之間
	 * getrandmax() 回傳 RAND_MAX 的值
	 */
	/**** 範例 ****/
	/*
		echo abs(-10), '<br>';
		echo ceil(7), '<br>;
		echo floor(4.1), '<br>';
		echo round(3.2, 1), '<br>';
	*/

	/*
	 * ---------- 字串轉換函式 ----------
	 *
	 * strtolower(str) 字串轉為小寫
	 * strtoupper(str) 字串轉為大寫
	 * ucfirst(str) 第一個字元轉為大寫
	 * ucwords(str) 每一單字的第一個字元轉為大寫
	 * ord(str) 傳回第一個字元的 ASCII 碼
	 * chr(int) 取得 ASCII 碼代表的字元
	 * strrev(str) 將字串的字元順序倒過來
	 */
	/**** 範例 ****/
	/*

	*/

	/*
	 * ---------- 字串比較函式 ----------
	 *
	 * strcmp(str1, str2) 若 str1 > str2，回傳值 > 0
	 					  若 str1 = str2，回傳值 = 0
	 					  若 str1 < str2，回傳值 < 0
	 * strncmp(str1, str2, n)  同 strcmp()，但只比前 n 個字元
	 *
	 * strcasecmp(str1, str2)      同 strcmp()，但不分大小寫
	 * strncasecmp(str1, str2, n)  同 strcasecmp()，但只比前 n 個字元
	 * 
	 */
	/**** 範例 ****/
	/*
		if (strcmp("a", "b")>0)
			echo '"a" > "b"<br>';
		elseif(strcmp("a", "b")==0)
			echo '"a" = "b"<br>';
		else
			echo '"a" < "b"<br>';
	
		if(strcmp("a", "A")!=0)
			echo '"a" != "A"<br>';
		if(strcasecmp("a", "A")==0)
			echo '"a" = "A"<br>';
	*/

	/*
	 * ---------- 字串取代函式 ----------
	 *
	 * str_replace(search, replace, subject [, &count]) 將 subject 字串中出現的 search 字串替換成 replace，
														count 是用來回傳總共替換幾次
	 * str_ireplace(search, replace, subject [, &count]) 同 str_replace，但不區分大小寫
	 *
	 */
	/**** 範例 ****/
	/*
		echo str_replace("foo", "bar", "my foo is always foo.", $count), "<br>";
		echo $count, "<br>";
	
		echo str_ireplace("foo", "bar", "my Foo is always foo.", $count), "<br>";
		echo $count, "<br>";
	
		echo str_replace(array('foo', 'is'), array('bars', 'are'), "my foo is always foo.", $count), "<br>";
		echo $count, "<br>";
	*/
	
	/*
	 * ---------- 字串尋找函式 ----------
	 *
	 * strstr(haystack, needle) 在 haystack 字串中找 needle 字串首次出現的地方，並回傳從該處開始之後的字串
	 * strchr(haystack, needle) 同 strstr()
	 * stristr(haystack, needle) strstr() 不分大小寫的版本
	 * strrchr(haystack, needle) strchr() 找最後一個的版本
	 *
	 * strpos(haystack, needle[, offset]) 回傳 needle 在 haystack 字串第一次出現的位置，offset 設定開始找的位置
	 * stripos(haystack, needle[, offset]) 不分大小寫的版本
	 *
	 * strrpos(haystack, needle[, offset]) 回傳 needle 在 haystack 字串最後一次出現的位置，offset 設定開始找的位置
	 * strripos(haystack, needle[, offset]) 不分大小寫的版本
	 *
	 */
	/**** 範例 ****/
	/*
		echo strrchr("my foo is always foo ...", "foo"), "<br>";
		echo strrpos("my foo is always foo ...", "foo", 18)==false, "<br>";
	*/


	/*
	 * ---------- 其他字串函式 ----------
	 * 
	 * strlen(str) 回傳字串長度
	 * str_repeat(str, count) 回傳 str 重複 count 次的字串
	 * substr(str, start[, length]) 回傳 str 從位置 start 開始的子字串，length 設定子字串長度
	 * ltrim(str[, charlist]) 將 str 左邊的空白刪去後回傳，若提供 charlist 字串則刪 charlist 中的字元
	 * rtrim(str[, charlist]) ltrim 右邊的版本
	 * chop(str[, charlist]) 同 rtrim()
	 * trim(str[, charlist])  ltrim() 加上 rtrim()
	 * nl2br(str) 等同 str_replace('\n', '<br>', subject)
	 *
	 */
	/**** 範例 ****/
	/*
		var_dump( ltrim('   fjiosdjifo', 'fdfas'));
	*/

	/*
	 * ---------- 字串與陣列轉換 ----------
	 * 
	 * implode(separator_str, arr) 將 arr 中的元素用 separator_str 連接形成字串
	 * join(separator_str, arr) 同 implode
	 *
	 * explode(separator_str, str[, limit]) 以 separator_str 為分割符號將 str 轉為字串，limit 表示最多切成幾個元素
	 */

	/*
	 * ---------- 陣列相關函式 ----------
	 * 
	 * is_array(arr) 判斷是否為陣列
	 * count(arr), sizeof(arr) 回傳 array 元素個數
	 * in_array(value, arr) 判斷 value 是否在 arr 中，會分大小寫
	 * unset(value) 清除陣列元素 value
	 *
	 * array_sum(arr) 傳回 arr 元素總和
	 * array_push(&arr, arg1[, arg2, ...]) 將 arg1 至 n 陸續加入 arr 尾端
	 * array_pop(&arr) 移除 arr 尾端元素
	 *
	 * asort(&arr)  將元素根據其值由小排到大
	 * arsort(&arr) 將元素根據其值由大排到小
	 * ksort(&arr)  將元素根據其 key 由小排到大
	 * krsort(&arr) 將元素根據其 key 由大排到小
	 *
	 * shuffle(&arr) 將 array 順序打亂
	 * 
	 */
	/**** 範例 ****/
	/*
		$a = array(NULL, 1, 2);
		var_dump($a);
		echo "<br>";
		unset($a[1]);
		var_dump($a);
	*/

	/*
	 * ---------- 日期時間函式 ----------
	 * 
	 * date_default_timezone_set(time_identifier) 設定時區，參數放 'Asia/Taipei' 則為台北時間
	 											  強烈建議使用時間相關函數前要設置
	 *
	 * time() 傳回目前時間的 UNIX 時間刻記
	 *
	 * mktime([hour[, minute[, second[, month[, day[, year[, is_dst]]]]]]])
	 		根據輸入的時間回傳相應的 timestamp
	 		is_dst 用來設定日光節約時間，是的話為 1，否則為 0
	 *
	 * date(format[, timestamp]) 傳回 format 字串規定的時間格式，
	 							 可參考 http://php.net/manual/en/function.date.php
	 * 
	 */
	/**** 範例 ****/
	/*
		date_default_timezone_set('Asia/Taipei');
		echo date('H:i:s');
	*/
?>