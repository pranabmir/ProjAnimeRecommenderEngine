import gcsfs

# Initialize filesystem (auto picks up GOOGLE_APPLICATION_CREDENTIALS)
fs = gcsfs.GCSFileSystem()

# Try listing the bucket
print("Listing bucket contents:")
print(fs.ls("projanimerecommenderdvc"))
