class PostPageConst:
    SUCCESS_MESSAGE_TEXT = 'New post successfully created.'
    POST_IS_CREATED_MESSAGE_XPATH = F"//div[text()='{SUCCESS_MESSAGE_TEXT}']"
    POST_TITLE_XPATH = ".//h2"
    POSTED_BY_XPATH = ".//p[@class='text-muted small mb-4']"
    POSTED_BY_MESSAGE = "Posted by {user_name} on {date}"
    POST_BODY_XPATH = ".//p[text()='{post_body}']"
