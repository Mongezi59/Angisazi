# 🔥 GitHub Actions - Automatic APK Build

**Push code to GitHub → APK builds automatically → Download and use!**

---

## 🎯 What Happens

```
You push to GitHub
         ↓
GitHub Actions sees the push
         ↓
Automatically runs buildozer
         ↓
Builds APK in the cloud (10-15 min)
         ↓
Uploads APK to Artifacts
         ↓
You download APK
         ↓
Done! ✅
```

---

## 📋 EXACT STEPS TO FOLLOW

### **STEP 1: Create GitHub Repository** (2 min)

1. Go to https://github.com/new
2. **Repository name:** `ghostforge-apk`
3. **Description:** GhostForge IDE APK Builder
4. **Make it PUBLIC** ← Important for free Actions!
5. Click "Create repository"

### **STEP 2: Download Files from Above** (1 min)

Download these 3 files:
- `main_working.py`
- `buildozer_working.spec`
- `.github_workflows_build.yml`

### **STEP 3: Rename Files**

Rename:
- `main_working.py` → `main.py`
- `buildozer_working.spec` → `buildozer.spec`

### **STEP 4: Create Folder Structure** (2 min)

On your computer:

```
ghostforge-apk/
├── main.py                    (from download)
├── buildozer.spec             (from download)
├── README.md                  (create below)
└── .github/
    └── workflows/
        └── build.yml          (from download)
```

### **STEP 5: Create README.md**

Create new file: `README.md`

```markdown
# GhostForge IDE - Automatic APK Build

## Build Instructions

1. Go to "Actions" tab
2. View build progress
3. When complete, download APK from Artifacts

## Install

```bash
adb install ghostforge-*.apk
```
```

### **STEP 6: Clone Repository**

```bash
# On your computer
git clone https://github.com/YOUR_USERNAME/ghostforge-apk.git
cd ghostforge-apk
```

### **STEP 7: Copy Files**

```
Copy these files into the ghostforge-apk folder:
- main.py
- buildozer.spec
- README.md
- .github/workflows/build.yml (create the .github and workflows folders)
```

### **STEP 8: Push to GitHub**

```bash
git add .
git commit -m "Initial commit: GhostForge IDE"
git push origin main
```

### **STEP 9: Watch Build Start**

1. Go to https://github.com/YOUR_USERNAME/ghostforge-apk
2. Click "Actions" tab
3. See "Build APK" workflow running
4. Wait 10-15 minutes

### **STEP 10: Download APK**

When build completes (green checkmark ✅):

1. Click the workflow name
2. Scroll down to "Artifacts"
3. Click "apk-build"
4. Your APK downloads!

---

## 📥 Install on Phone

### Option A: Via USB (adb)

```bash
adb devices
adb install -r ghostforge-1.0.0-release-unsigned.apk
```

### Option B: Manual

1. Transfer APK to phone
2. Open file manager
3. Tap the APK
4. Tap "Install"

---

## 🔄 Rebuild Anytime

Just push new code:

```bash
# Make changes to main.py (or other files)
git add main.py
git commit -m "Update: [your changes]"
git push origin main

# GitHub Actions automatically rebuilds!
# Check Actions tab for new build
```

---

## ✅ File Checklist

Before pushing, verify you have:

- [ ] `main.py` ← Your Kivy app
- [ ] `buildozer.spec` ← Build configuration
- [ ] `README.md` ← Documentation
- [ ] `.github/workflows/build.yml` ← GitHub Actions config
- [ ] `.git/` folder ← Created by `git clone`

---

## ⏱️ Build Times

| Step | Time |
|------|------|
| GitHub setup | 2 min |
| File download | 1 min |
| File setup | 2 min |
| Git push | 1 min |
| First build | 15-20 min |
| Rebuild (cached) | 10-15 min |

**Total first time: ~25 minutes**

---

## 🆘 Troubleshooting

### "Build failed - NDK not found"
- This is normal on first build
- Click "Re-run jobs" in Actions tab
- Try again

### "Build succeeded but no APK"
- Check the workflow ran successfully (green ✅)
- Click workflow
- Look for Artifacts section
- If missing, check build log for errors

### "Private repo won't build"
- GitHub Actions is free only on PUBLIC repos
- Make repo public:
  - Settings → General → Change to Public
  - Or create new PUBLIC repo

### "APK file is huge"
- First build: 40-50 MB (normal)
- Later builds: smaller (with cache)

---

## 📖 What Each File Does

### **main.py**
Your actual Kivy application
- Chat interface
- Terminal emulator
- Code editor
- Build management

### **buildozer.spec**
Configuration for building APK
- App name, version, permissions
- Android API levels
- Dependencies

### **build.yml** (GitHub Actions)
Instructions for GitHub to build
- Install dependencies
- Run buildozer
- Upload APK to Artifacts

---

## 🎯 Quick Reference

```bash
# First time setup
git clone https://github.com/YOUR_USERNAME/ghostforge-apk.git
cd ghostforge-apk
# Copy main.py, buildozer.spec, README.md, .github/ here
git add .
git commit -m "Initial"
git push origin main

# Rebuild later
git add .
git commit -m "Update"
git push origin main
```

---

## ✨ You're Ready!

1. ✅ Create GitHub repo (PUBLIC)
2. ✅ Add files
3. ✅ Push to GitHub
4. ✅ GitHub Actions builds
5. ✅ Download APK
6. ✅ Install on phone

**That's all!** 🔥👑

---

## 🤔 Questions?

- **GitHub:** https://docs.github.com/actions
- **Buildozer:** https://buildozer.readthedocs.io
- **Kivy:** https://kivy.org

Good luck! 🚀
