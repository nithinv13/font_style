FILE="common_words_four_books.txt"
i=1
exec 0<"$FILE"
n=0
while read -r line
do
   a="$line"
   
   convert -background white -fill black -font /usr/share/fonts/truetype/msttcorefonts/arial.ttf -pointsize 30 -fill black -gravity center label:"$a" "$i".tif 
   i=$(($i + 1)) 
done



