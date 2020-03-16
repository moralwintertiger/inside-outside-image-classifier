# Code forked from https://github.com/gsssrao/youtube-8m-videos-frames

# Check number of arguments
if [ "$#" != "3" ]; then
	echo "Usage: bash downloadmulticategoryvideos.sh <number-of-vids-per-category> <output-directory> <selected-category-file-name>"
	exit 1
fi

while read line
	do
		bash downloadcategoryids.sh $1 "${line}"
		bash downloadvideos.sh $1 $2 "${line}"
	done < "$3"
