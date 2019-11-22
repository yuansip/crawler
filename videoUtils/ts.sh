#!/bin/bash
for i in {1..31}
do
    if [ $i -eq 9 ]
    then
        continue
    fi
    echo "transfer $i.ts"
    ffmpeg -i $i.ts -c:v copy -c:a copy $i.mp4
done

# ffmpeg -i 1.ts -c:v copy -c:a copy 3.mp4
# ffmpeg -i 2.ts -c:v copy -c:a copy 3.mp4
# ffmpeg -i 3.ts -c:v copy -c:a copy 3.mp4
# ffmpeg -i 4.ts -c:v copy -c:a copy 4.mp4
# ffmpeg -i 5.ts -c:v copy -c:a copy 5.mp4
# ffmpeg -i 6.ts -c:v copy -c:a copy 6.mp4
# ffmpeg -i 7.ts -c:v copy -c:a copy 7.mp4
# ffmpeg -i 8.ts -c:v copy -c:a copy 8.mp4
# ffmpeg -i 9.ts -c:v copy -c:a copy 9.mp4
# ffmpeg -i 10.ts -c:v copy -c:a copy 10.mp4
# ffmpeg -i 11.ts -c:v copy -c:a copy 11.mp4
# ffmpeg -i 12.ts -c:v copy -c:a copy 12.mp4
# ffmpeg -i 13.ts -c:v copy -c:a copy 13.mp4
# ffmpeg -i 14.ts -c:v copy -c:a copy 14.mp4
# ffmpeg -i 15.ts -c:v copy -c:a copy 15.mp4
# ffmpeg -i 16.ts -c:v copy -c:a copy 16.mp4
# ffmpeg -i 17.ts -c:v copy -c:a copy 17.mp4
# ffmpeg -i 18.ts -c:v copy -c:a copy 18.mp4
# ffmpeg -i 19.ts -c:v copy -c:a copy 19.mp4