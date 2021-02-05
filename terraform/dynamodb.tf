# ----------------------
#
# Setup Dynamo DB tables
#
# ----------------------

##
# Skills table
###
resource "aws_dynamodb_table" "skills_table" {
  name           = var.dynamodb_skills_table_name
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "category"
  range_key      = "name"
  tags           = merge(var.aws_resource_tags, var.dynamodb_skills_table_tags)

  attribute {
    name = "category"
    type = "S"
  }
  attribute {
    name = "name"
    type = "S"
  }
}
