## Git Large Files
```bash
git lfs install
```

## In each Git repository where you want to use Git LFS, select the file types you'd like Git LFS to manage (or directly edit your .gitattributes). You can configure additional file extensions at anytime.
```bash
git lfs track "*.psd"
```

## Now make sure .gitattributes is tracke
```bash
git add .gitattributes
```
## There is no step three. Just commit and push to GitHub as you normally would; for instance, if your current branch is named main:
```bash
git add file.psd
git commit -m "Add design file"
git push origin main
```
