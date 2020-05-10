mkdir -p converted
for i in wavs/*.wav; do
    o=converted/${i#wavs/}
    sox "$i" -r 22050 -c 1 "${o%}"
done
