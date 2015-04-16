from mock import patch, MagicMock
from nose.tools import assert_equal
import outbrain
import unittest
import yaml


class TestOutbrainAmplifyApi(unittest.TestCase):
    """
    Test suite for OutbrainAmplifyApi class
    """

    @patch('outbrain.OutbrainAmplifyApi.get_token')
    def test_init(self, get_token_mock):
        get_token_mock.return_value = 'token_mock'
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        get_token_mock.assert_called_with('user', 'pass')
        assert_equal(api.token, "token_mock")

    @patch('requests.get')
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock(return_value="token_mock"))
    def test_request(self, requests_get_mock):
        requests_get_mock.return_value = create_mock_request_result()

        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        assert_equal(api.token, "token_mock")
        result = api._request('path_mock', 'params_mock')
        assert_equal(result, {'request_key': 'request_value'})

    @patch('requests.get')
    def test_get_token(self, requests_get_mock):
        requests_get_mock.return_value = create_mock_token()

        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        assert_equal(api.token, {"mock_key": "mock_value"})

    @patch('requests.get', MagicMock())
    @patch('outbrain.OutbrainAmplifyApi._yield_promoted_links_for_campaign',
           MagicMock(return_value=[1, 'b', 3]))
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_promoted_links_for_campaign(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        result = api.get_promoted_links_for_campaign('campaign_id_mock')
        assert_equal(result, [1, 'b', 3])

#--------------------------------------------------------------------------------------------------
# Utility methods to ease mocking objects
#--------------------------------------------------------------------------------------------------
def create_mock_token():
    token = MagicMock()
    token.text = '{"OB-TOKEN-V1": {"mock_key": "mock_value"}}'
    return token

def create_mock_request_result():
    result = MagicMock()
    result.text = '{"request_key": "request_value"}'
    return result

