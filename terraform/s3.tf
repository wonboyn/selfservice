# ---------------------
#
# Setup S3 Buckets
#
# ---------------------

###
# S3 Bucket for Lambda source
###
resource "aws_s3_bucket" "s3_bucket_lambda_source" {
  bucket    = var.root_bot_lambda_source_s3_bucket_name
  tags      = var.aws_resource_tags
  versioning {
    enabled = true
  }
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}


###
# Restrict public access to the bucket
###
resource "aws_s3_bucket_public_access_block" "s3_bucket_lambda_source_public_access" {
  bucket = aws_s3_bucket.s3_bucket_lambda_source.id

  block_public_acls       = true
  block_public_policy     = true
  restrict_public_buckets = true
}