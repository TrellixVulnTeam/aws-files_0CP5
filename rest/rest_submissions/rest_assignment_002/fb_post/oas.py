{
    "swagger": "2.0",
    "host": "localhost:8000",
    "basePath": "/fb_post/",
    "info": {
        "version": "1.0.0",
        "title": "Simple API",
        "description": "A simple API to learn how to write OpenAPI Specification"
    },
    "schemes": [
        "https",
        "http"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "oauth": {
            "tokenUrl": "http://auth.ibtspl.com/oauth2/",
            "flow": "password",
            "scopes": {
                "read": "read users",
                "write": "create users",
                "update": "update users",
                "delete": "delete users",
                "superuser": "super user permission" 
            },
            "type": "oauth2"
        }
    },

    "definitions": {

        "User": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "name": {
                    "type": "string",
                },
                "profile_pic": {
                    "type": "string"
                }
            },
        },

        "UserReaction": {
            "allOf": [
                {
                "$ref": "#/definitions/User"
                },
                {
                    "type": "object",
                    "properties": {
                        "reaction": {
                            "type": "string",
                            "enum": [
                                'WOW', 'LIT',
                                'LOVE', 'HAHA',
                                'THUMBS-UP', 'THUMBS-DOWN',
                                'ANGRY', 'SAD'
                            ]
                        }
                    }
                }
            ]
        },

        "Reactions": {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "format": "int64"
                },
                "type": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                }
            },
        },

        "Comment": {
            "type": "object",
            "properties": {
                "comment_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "commenter": {
                    "$ref": "#/definitions/User"
                },
                "commented_at": {
                    "type": "string",
                    "format": "datetime"
                },
                "comment_content": {
                    "type": "string"
                },
            },
        },

        "ReplyComment": {
            "allOf": [
                {
                    "$ref": "#/definitions/Comment"
                },
                {
                    "type": "object",
                    "properties": {
                        "reactions": {
                            "$ref": "#/definitions/Reactions"
                        },
                    },
                }
            ]
        },

        "Comments": {
            "allOf": [
                {
                    "$ref": "#/definitions/Comment"
                },
                {
                    "type": "object",
                    "properties": {
                        "reactions": {
                            "$ref": "#/definitions/Reactions"
                        },
                        "replies_count": {
                            "type": "integer",
                            "format": "int64"
                        },
                        "replies": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/ReplyComment"
                            }
                        }
                    }
                }
            ]
        },

        "Post": {
            "type": "object",
            "properties": {
                "post_id": {
                    "type": "integer",
                    "format": "int64"
                },
                "posted_by": {
                    "$ref": "#/definitions/User"
                },
                "posted_at": {
                    "type": "string",
                    "format": "datetime"
                },
                "post_content": {
                    "type": "string"
                },
                "reactions": {
                    "$ref": "#/definitions/Reactions"
                },
                "comments": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Comments"
                    }
                },
                "comments_count": {
                    "type": "integer",
                    "format": "int64"
                }
            }
        },
    },

    "parameters": {
        "CreatePostParameter": {
            "name": "post",
            "in": "body",
            "required": True,
            "description": "create a post",
            "schema": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string"
                    }
                },
                "required": [
                    "content"
                ]
            }
        },

        "CreateReactionParameter": {
            "name": "post",
            "in": "body",
            "required": True,
            "description": "create a reaction",
            "schema": {
                "type": "object",
                "properties": {
                    "reaction_type": {
                        "type": "string",
                        "enum": [
                            'WOW', 'LIT',
                            'LOVE', 'HAHA',
                            'THUMBS-UP', 'THUMBS-DOWN',
                            'ANGRY', 'SAD'
                        ]
                    }
                },
                "required": [
                    "reaction_type"
                ]
            }
        },

        "DeletePostParameter": {
            "name": "post",
            "in": "body",
            "required": True,
            "description": "delete a post",
            "schema": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "format": "int64"
                    }
                },
                "required": [
                    "user_id"
                ]
            }
        },
    },

    "responses": {

        "CreatePostResponse": {
            "description": "Success Response",
            "schema": {
                "properties": {
                    "post_id": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            }
        },

        "CreateCommentResponse": {
            "description": "Success Response",
            "schema": {
                "properties": {
                    "comment_id": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            }
        },

        "Raise400error": {
            "description": "Invalid Content"
        },

        "Raise404error": {
            "description": "Invalid id"
        },

        "Raise403error": {
            "description": "Unauthorized user"
        },

        "PostDetailResponse": {
            "description": "Success Response",
            "schema": {
                "$ref": "#/definitions/Post"
            }
        },

        "UserPostDetailResponse": {
            "description": "Success Response",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/Post"
                }
            },
        },

        "PostIdsResponse": {
            "description": "Success Response",
            "schema": {
                "type": "array",
                "items": {
                    "type": "integer",
                    "format": "int64"
                }
            },
        },

        "ReactionsCountResponse": {
            "description": "Success Response",
            "schema": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            },
        },

        "ReactionMetricsResponse": {
            "description": "Success Response",
            "schema": {
                "type": "object",
                "properties": {
                    "reaction_type": {
                        "type": "string",
                        "enum": [
                            'WOW', 'LIT',
                            'LOVE', 'HAHA',
                            'THUMBS-UP', 'THUMBS-DOWN',
                            'ANGRY', 'SAD'
                        ]
                    },
                    "count": {
                        "type": "integer",
                        "format": "int64"
                    }
                }
            },
        },

        "PostReactionsResponse": {
            "description": "Success Response",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/UserReaction",
                }
            },
        },

        "CommentRepliesResponse": {
            "description": "Success Response",
            "schema": {
                "$ref": "#/definitions/Comment"
            }
        }

    },

    "paths": {

        "/post/create/v1/": {
            "post": {
                "operationId": "create_post",
                "summary": "Create New Post",
                "description": "Create New Post and return Post id",
                "security": [
                    {
                        "oauth": [
                            "write"
                        ]
                    }
                ],
                "parameters": [
                    {
                        "$ref": "#/parameters/CreatePostParameter"
                    }
                ],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreatePostResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "400": {
                        "$ref": "#/responses/Raise400error"
                    }
                }
            }
        },

        "/post/{post_id}/comment/create/v1/": {
            "post": {
                "operationId": "create_comment",
                "summary": "Create New Comment",
                "description": "Create New Comment and return Comment id",
                "security": [
                    {
                        "oauth": [
                            "read",
                            "write"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "post_id",
            "in": "path",
            "required": True,
            "description": "The post's id",
            "type": "integer",
            "format": "int64",
          },
          {
              "$ref": "#/parameters/CreatePostParameter"
          }
                ],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreateCommentResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "400": {
                        "$ref": "#/responses/Raise400error"
                    }
                }
            }
        },

        "/comment/{comment_id}/reply/create/v1/": {
            "post": {
                "operationId": "create_reply_comment",
                "summary": "Create New Reply Comment",
                "description": "Create New Reply Comment and return Comment id",
                "security": [
                    {
                        "oauth": [
                            "read",
                            "write"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "comment_id",
            "in": "path",
            "required": True,
            "description": "The comment's id",
            "type": "integer",
            "format": "int64",
          },
          {
             "$ref": "#/parameters/CreatePostParameter"
          }
                ],
                "responses": {
                    "201": {
                        "$ref": "#/responses/CreateCommentResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "400": {
                        "$ref": "#/responses/Raise400error"
                    }
                }
            }
        },

        "/post/{post_id}/react/v1/": {
            "post": {
                "operationId": "create_post_reaction",
                "summary": "Create Reation To Post",
                "description": "Create Post's Reaction",
                "security": [
                    {
                        "oauth": [
                            "read",
                            "write"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "post_id",
            "in": "path",
            "required": True,
            "description": "The post's id",
            "type": "integer",
            "format": "int64",
          },
          {
             "$ref": "#/parameters/CreateReactionParameter"
          }
                ],
                "responses": {
                    "200": {
                        "description": "Response Success"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "400": {
                        "$ref": "#/responses/Raise400error"
                    }
                }
            }
        },

        "/comment/{comment_id}/react/v1/": {
            "post": {
                "operationId": "create_comment_reaction",
                "summary": "Create Reation To Comment",
                "description": "Create Comment's Reaction",
                "security": [
                    {
                        "oauth": [
                            "read",
                            "write"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "comment_id",
            "in": "path",
            "required": True,
            "description": "The comment's id",
            "type": "integer",
            "format": "int64",
          },
          {
             "$ref": "#/parameters/CreateReactionParameter"
          }
                ],
                "responses": {
                    "200": {
                        "description": "Response Success"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "400": {
                        "$ref": "#/responses/Raise400error"
                    }
                }
            }
        },

        "/post/{post_id}/delete/v1/": {
            "post": {
                "operationId": "delete post",
                "summary": "Delete Post",
                "description": "Delete",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "post_id",
            "in": "path",
            "required": True,
            "description": "The post's id",
            "type": "integer",
            "format": "int64",
          },
          {
             "$ref": "#/parameters/DeletePostParameter"
          }
                ],
                "responses": {
                    "200": {
                        "description": "Response Success"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    },
                    "403": {
                        "$ref": "#/responses/Raise403error"
                    }
                }
            }
        },

        "/post/{post_id}/details/v1/": {
            "get": {
                "operationId": "post_details",
                "summary": "Get Post Information",
                "description": "Get Post",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "post_id",
            "in": "path",
            "required": True,
            "description": "The post's id",
            "type": "integer",
            "format": "int64",
          },
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/PostDetailResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    }
                }
            }
        },

        "/user/posts/v1/": {
            "get": {
                "operationId": "user_posts_details",
                "summary": "Get User Posts Information",
                "description": "Get User Posts",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/UserPostDetailResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    }
                }
            }
        },

        "/user/react/posts/v1/": {
            "get": {
                "operationId": "user_reacted_posts",
                "summary": "Get User Reacted Posts Information",
                "description": "Get User Reacted Posts",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/PostIdsResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    }
                }
            }
        },

        "/reactions/count/v1/": {
            "get": {
                "operationId": "reactions_count",
                "summary": "Get Total Reactions",
                "description": "Get Total Reactions Count",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/ReactionsCountResponse"
                    }
                }
            }
        },

        "/reactions/metrics/v1/": {
            "get": {
                "operationId": "reactions_metrics",
                "summary": "Get Reactions Metrics",
                "description": "Get Reactions Metrics",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/ReactionMetricsResponse"
                    }
                }
            }
        },

        "/post/{post_id}/reactions/v1/": {
            "get": {
                "operationId": "post_reactions",
                "summary": "Get Post Reactions",
                "description": "Get Post Reactions",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "post_id",
            "in": "path",
            "required": True,
            "description": "The post's reactions",
            "type": "integer",
            "format": "int64",
          },
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/PostReactionsResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    }
                }
            }
        },

        "/comment/{comment_id}/replies/v1/": {
            "get": {
                "operationId": "comment_replies",
                "summary": "Get Comment Replies",
                "description": "Get Comment Replies",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "parameters": [
                    {
            "name": "comment_id",
            "in": "path",
            "required": True,
            "description": "The comment's replies",
            "type": "integer",
            "format": "int64",
          },
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/CommentRepliesResponse"
                    },
                    "404": {
                        "$ref": "#/responses/Raise404error"
                    }
                }
            }
        },

        "/post/positive/reactions/v1/": {
            "get": {
                "operationId": "positive_reactions",
                "summary": "Get Posts With More Positive Reactions",
                "description": "Get Posts With Positive Reactions",
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "responses": {
                    "200": {
                        "$ref": "#/responses/PostIdsResponse"
                    }
                }
            }
        },

    }
}