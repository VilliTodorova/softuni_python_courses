from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia(
            "test",
            "Instagram",
            50,
            "reel"
        )

    def test_correct_init(self):
        self.assertEqual("test", self.social_media._username)
        self.assertEqual("Instagram", self.social_media.platform)
        self.assertEqual(50, self.social_media.followers)
        self.assertEqual("reel", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_invalid_platform_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "facebook"

        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        expected = f"Platform should be one of {allowed_platforms}"

        self.assertEqual(expected, str(ve.exception))

    def test_setting_valid_platform(self):
        self.social_media.platform = "YouTube"

        self.assertEqual("YouTube", self.social_media._platform)

    def test_setting_followers_negative_quantity_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -10

        expected = "Followers cannot be negative."

        self.assertEqual(expected, str(ve.exception))

    def test_setting_followers_edge_case_zero(self):
        self.social_media.followers = 0

        self.assertEqual(0, self.social_media._followers)

    def test_creating_a_post_correct_list_representation(self):
        self.social_media.create_post("funny cat")

        self.assertEqual([{'content': "funny cat", 'likes': 0, 'comments': []}], self.social_media._posts)

    def test_creating_a_post_correct_return_message(self):
        result = self.social_media.create_post("funny cat")
        expected = "New reel post created by test on Instagram."

        self.assertEqual(expected, result)

    def test_liking_a_post_one_post_available_like_accepted(self):
        self.social_media.create_post("funny cat")
        self.social_media.like_post(0)

        self.assertEqual(1, self.social_media._posts[0]["likes"])

    def test_liking_a_post_one_post_available_like_not_accepted(self):
        self.social_media.create_post("funny cat")
        self.social_media._posts[0]["likes"] = 10

        result = self.social_media.like_post(0)
        expected = "Post has reached the maximum number of likes."

        self.assertEqual(expected, result)

    def test_liking_post_invalid_index_message(self):
        self.social_media.create_post("funny cat")
        self.social_media.create_post("funny dog")

        expected = "Invalid post index."
        result = self.social_media.like_post(2)

        self.assertEqual(expected, result)

    def test_commenting_on_post_valid_index_sufficient_len_list_repr(self):
        self.social_media.create_post("funny dog")
        self.social_media.comment_on_post(0, "this is a very cute puppy")

        self.assertEqual([{'user': "test", 'comment': "this is a very cute puppy"}],
                         self.social_media._posts[0]["comments"])

    def test_commenting_on_post_valid_index_sufficient_len_return_message(self):
        self.social_media.create_post("funny dog")

        result = self.social_media.comment_on_post(0, "this is a very cute puppy")
        expected = "Comment added by test on the post."

        self.assertEqual(expected, result)

    def test_commenting_on_post_insufficient_len_return_message(self):
        self.social_media.create_post("funny dog")

        result = self.social_media.comment_on_post(0, "cute")
        expected = "Comment should be more than 10 characters."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
