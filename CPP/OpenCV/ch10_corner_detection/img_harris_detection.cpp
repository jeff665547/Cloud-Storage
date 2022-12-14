/* Harris 角點偵測 */
// 角點檢測(Corner Detection)是電腦視覺系統中用來獲得影像特徵的一種方法，
// 廣泛應用於運動檢測、影像匹配、視訊跟蹤、三維模型和目標識別等領域，也被稱為特徵點檢測。
// 角點通常被定義為兩條邊的交點，更嚴格地說法是，角點的局部鄰域應該具有兩個不同區域的不同方向的邊界。
// 實際應用中，大多數所謂的角點檢測方法檢測的是擁有特定特徵的影像點。而不僅僅是"角點"。
// 這些特徵點在影像中有具體的座標，並具有某些數學特徵，如局部最大或最小灰階、某些梯度特徵等。
// 在影像處理和電腦視覺領域，興趣點(Interest points)也被稱為關鍵點(key points)、特徵點(feature points)。
// 它被大量用於解決物體識別、影像識別、影像匹配、視覺跟蹤、三維重建等一系列的問題。
// 我們不再觀察整幅圖，而是選擇某些特殊的點，然後對這些點進行局部的分析。
// 如果能檢測到足夠多的這種點，同時它們的區分度很高，並且可以精確定位穩定的特徵，
// 那麼這個方法就具有實用價值。
// 影像特徵類型可以被分為如下三種：
// 1. 邊緣
// 2. 角點(感興趣關鍵點)
// 3. 斑點(Blobs)(感興趣區域)
// 其中，角點是個很特殊的存在。
// 如果某一點在任意方向的一個微小變動都會引起灰階很大的變化，那麼我們就把它稱之為角點。
// 角點包含有重要的資訊，在影像融合和目標跟蹤及三維重建中有重要的應用價值。
// 他們在影像中可以輕易地定位，同時，在人造物體場景，比如門、窗、桌等處也隨處可見。
// 因為角點位於兩條邊緣的焦點處，代表了兩個邊緣變化的方向上的點，
// 所以它們是可以精確定位的二維特徵，甚至可以達到亞像素的精度。
// 角點與位於相同強度區域上的點不同，與物體輪廓上的點也不同，
// 因為輪廓點難以在相同的其他物體上精確定位。
// 關於角點的具體描述可以有如下幾種：
// 1. 一階導數(及灰階的梯度)的局部最大所對應的像素點。
// 2. 兩條及兩條以上邊緣的交點。
// 3. 影像中梯度值和梯度方向的變化速率都很高的點
// 4. 角點處的一階導數最大，二階導數為零，它指示了物體邊緣變化不連續的方向。
int main(){

    return 0;
}