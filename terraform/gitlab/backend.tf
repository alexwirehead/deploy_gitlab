terraform {
  backend "gcs" {
    bucket  = "wirehead_tf_state"
    prefix  = "terraform_gitlab_state"
  }
}