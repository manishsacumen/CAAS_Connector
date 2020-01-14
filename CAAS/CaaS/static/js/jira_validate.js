$(document).ready(function() {
    $("#basic-form").validate({
      rules: {
        app_url : {
          required: true,
        },
        api_key: {
          required: true,
        },
        email: {
          required: true,
          email: true
        },
        project_key: {
          required: true,
        }
      },
      messages : {
        app_url: {
          required: "App Url is required"
        },
        api_key: {
          required: "Api Key is required",
        },
        email: {
          required: "Email is required",
          email: "The email should be in the format: abc@domain.tld"
        },
        project_key: {
          required: "Project Key is required",

        }
      }
    });
  });

