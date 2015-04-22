from mock import patch, MagicMock
from nose.tools import assert_equal, assert_raises, assert_true

import datetime
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
        assert_true(isinstance(result, dict))
        assert_equal(result, {'request_key': 'request_value'})

    @patch('requests.get')
    def test_get_token(self, requests_get_mock):
        requests_get_mock.return_value = create_mock_token()

        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        assert_equal(api.token, {"mock_key": "mock_value"})

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_marketer(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        api._request = MagicMock(return_value='result_mock')
        assert_raises(TypeError, api.get_marketer) # needs an argument
        result = api.get_marketer('my_id')
        api._request.assert_called_with('marketers/my_id')
        assert_equal(result, 'result_mock')

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_all_marketer_ids(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        api.get_marketers = MagicMock(return_value=[{'id': 1}, {'id': 2}])
        res = api.get_marketer_ids()
        assert_equal(res, [1, 2])

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_budget(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        api._request = MagicMock(return_value='result_mock')
        assert_raises(TypeError, api.get_budget) # needs an argument
        result = api.get_budget('my_budget_id')
        api._request.assert_called_with('budgets/my_budget_id')
        assert_equal(result, 'result_mock')

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_budgets_per_marketer(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        api._request = MagicMock()
        marketer_ids = []
        api.get_budgets_per_marketer([])
        assert_equal(api._request.call_count, 0)

        api._request = MagicMock(return_value={'budgets': 'budget_mock'})
        result = api.get_budgets_per_marketer(['foo'])
        assert_equal(api._request.call_count, 1)
        api._request.assert_called_with('/marketers/foo/budgets')
        assert_equal(result, {'foo': 'budget_mock'})

        api._request = MagicMock()
        marketer_ids = [m for m in range(42)]
        api.get_budgets_per_marketer(marketer_ids)
        assert_equal(api._request.call_count, len(marketer_ids))

    @patch('outbrain.OutbrainAmplifyApi._request')
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_campaign(self, _request_mock):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        path = 'campaigns/campaign_id_mock'
        _request_mock.return_value = '_request_return_mock'
        result = api.get_campaign('campaign_id_mock')
        _request_mock.assert_called_with(path)
        assert_equal(result, _request_mock.return_value)

    @patch('outbrain.OutbrainAmplifyApi._request')
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_campaign_ids(self, _request_mock):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        api._yield_all_campaigns = MagicMock(return_value= [])
        res = api.get_campaign_ids()
        assert_equal(res, [])

        api._yield_all_campaigns = MagicMock(return_value= [{'id': 'x'}, {'id': 'y'}])
        res = api.get_campaign_ids()
        assert_equal(res, ['x', 'y'])

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_campaigns_per_budget(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        api._request = MagicMock()
        api.get_campaigns_per_budget([])
        assert_equal(api._request.call_count, 0)

        api._request = MagicMock(return_value={'campaigns': 'budget_mock'})
        result = api.get_campaigns_per_budget(['foo'])
        assert_equal(api._request.call_count, 1)
        api._request.assert_called_with('budgets/foo/campaigns')
        assert_equal(result, {'foo': 'budget_mock'})

        api._request = MagicMock()
        budget_ids = [b for b in range(7)]
        api.get_campaigns_per_budget(budget_ids)
        assert_equal(api._request.call_count, len(budget_ids))

    @patch('outbrain.OutbrainAmplifyApi._request')
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_campaigns_per_marketer(self, _request_mock):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        path = 'marketers/abc123/campaigns'

        assert_raises(TypeError, api.get_campaigns_per_marketer)

        _request_mock.reset_mock()
        api.get_campaigns_per_marketer([])
        assert not _request_mock.called

        _request_mock.reset_mock()
        api.get_campaigns_per_marketer(['abc123'])
        _request_mock.assert_called_with(path, {'includeArchived': 'true'})

        _request_mock.reset_mock()
        api.get_campaigns_per_marketer(['abc123'], include_archived=True)
        _request_mock.assert_called_with(path, {'includeArchived': 'true'})

        _request_mock.reset_mock()
        api.get_campaigns_per_marketer(['abc123'], include_archived=False)
        _request_mock.assert_called_with(path, {'includeArchived': 'false'})

    @patch('requests.get', MagicMock())
    @patch('outbrain.OutbrainAmplifyApi._yield_promoted_links_for_campaign',
           MagicMock(return_value=[1, 'b', 3]))
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_promoted_links_for_campaign(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)
        result = api.get_promoted_links_for_campaign('campaign_id_mock')
        assert_equal(result, [1, 'b', 3])

    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_page_performance_data(self):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        start = datetime.datetime(year=2015, month=4, day=1, hour=13, minute=42)
        end = datetime.datetime(year=2015, month=4, day=3, hour=19, minute=24)
        path = 'marketers/marketer_id_mock/performanceByPublisher'
        params = {'to': '2015-04-01', 'from': '2015-04-03', 'limit': 20, 'offset': 3}

        path = 'marketers/marketer_id_mock/performanceByPublisher'
        params = {'from': '2015-04-01', 'to': '2015-04-03', 'limit': 20, 'offset': 3}
        api._request = MagicMock(return_value={})
        result = api._get_performance_data(path, start, end, 20, 3)
        api._request.assert_called_with(path, params)
        assert_equal(result, [])

        api._request = MagicMock(return_value={'details': 'details_mock'})
        result = api._get_performance_data(path, start, end, 20, 3)
        api._request.assert_called_with(path, params)
        assert_equal(result, 'details_mock')

    @patch('requests.get', MagicMock())
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    @patch('outbrain.OutbrainAmplifyApi._request')
    def test_page_promoted_links_for_campaign(self, _request_mock):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        _request_mock.reset_mock()
        _request_mock.return_value = {'promotedLinks': []}
        path = 'campaigns/123abc/promotedLinks'
        res = api._page_promoted_links_for_campaign(path, True, [], 10, 0)
        params = {'enabled': 'true', 'limit': 10, 'offset': 0}
        _request_mock.assert_called_with(path, params)
        assert_equal(res, [])
        
        _request_mock.reset_mock()
        _request_mock.return_value = {'promotedLinks': [1, 2, 'c']}
        path = 'campaigns/a1b2c3/promotedLinks'
        res = api._page_promoted_links_for_campaign(path, False, ['APPROVED', 'PENDING'], 12, 2)
        params = {'enabled': 'false', 'limit': 12, 'offset': 2, 'statuses': 'APPROVED,PENDING'}
        _request_mock.assert_called_with(path, params)
        assert_equal(res, [1, 2, 'c'])

        _request_mock.return_value = {'foo': 2}
        path = 'campaigns/a1b2c3/promotedLinks'
        res = api._page_promoted_links_for_campaign(path, None, ['PENDING'], 15, 5)
        params = {'limit': 15, 'offset': 5, 'statuses': 'PENDING'}
        _request_mock.assert_called_with(path, params)
        assert_equal(res, [])

    @patch('outbrain.OutbrainAmplifyApi._request')
    @patch('outbrain.OutbrainAmplifyApi.get_token', MagicMock())
    def test_get_campaign(self, _request_mock):
        config = yaml.load(open('outbrain.yml.example', 'r'))
        api = outbrain.OutbrainAmplifyApi(outbrain_config=config)

        path = 'currencies'
        _request_mock.return_value = {}
        result = api.get_currencies()
        _request_mock.assert_called_with(path)
        assert_equal(result, [])

        _request_mock.return_value = {'currencies': 'currency_list_mock'}
        result = api.get_currencies()
        _request_mock.assert_called_with(path)
        assert_equal(result, 'currency_list_mock')


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

