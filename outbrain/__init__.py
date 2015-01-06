
from dateutil.parser import parse
from datetime import datetime, timedelta
import requests
import json
import csv 
import yaml

class OutbrainAmplifyApi(object):

	def __init__(self):
		outbrain_config = yaml.load(open('outbrain.yml', 'r'))
		self.user = outbrain_config['user']
		self.password = outbrain_config['password']
		self.base_url = outbrain_config['base_url']
		self.token = self.get_token(self.user, self.password)

	def _request(self, path, params={}):
		url = self.base_url + path
		r = requests.get(url, headers={'OB-TOKEN-V1': self.token},
			params=params) 
		return json.loads(r.text)

	def get_token(self, user, password):
		token_url = self.base_url + '/login'
		r = requests.get(token_url, auth=(user, password))
		results = json.loads(r.text)
		return results['OB-TOKEN-V1']

	def get_marketers(self):
		path = 'marketers'
		results = self._request(path)
		return results['marketers']

	def get_budgets_per_marketer(self, marketing_ids):
		budgets = {}
		for marketing_id in marketing_ids:
			path = '/marketers/' + marketing_id + '/budgets'
			results = self._request(path)
			marketer_budgets = results['budgets']
			budgets[marketing_id] = marketer_budgets
		return budgets

	def get_campaigns_per_budget(self, budget_ids):
		campaigns = {}
		for budget_id in budget_ids:
			path = 'budgets/' + budget_id + '/campaigns'
			results = self._request(path)			
			budget_campaigns = results['campaigns']
			campaigns[budget_id] = budget_campaigns
		return campaigns

	def get_campaigns_per_marketer(self, marketing_ids):
		campaigns = {}
		for marketing_id in marketing_ids:
			path = 'marketers/' + marketing_id + '/campaigns'
			params = {'includeArchived': True}
			results = self._request(path, params)			
			marketer_campaigns = results['campaigns']
			campaigns[marketing_id] = marketer_campaigns
		return campaigns

	def get_links_per_budget(self, campaign_ids):
		promoted_links = {}
		for campaign_id in campaign_ids:
			promoted_links[campaign_id] = []
			count = 0
			total_count = None
			path = 'campaigns/' + campaign_id + '/promotedLinks'
			while not total_count or count < total_count:
				params = {'offset': max(count-1,0), 'sort': '-creationTime', 'statuses': 'APPROVED'}
				results = self._request(path, params)
				current_count = results['count']
		
				# unexpected
				if current_count <= 0: break

				count += current_count
				if not total_count:
					total_count = results['totalCount']

				promoted_links[campaign_id] += results['promotedLinks']
		return promoted_links

	def get_daily_performance(self, promoted_link_ids, start_day=None, end_day=None):
		if not end_day:
			end_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)	
		if not start_day:
			start_day = end_day - timedelta(days=1)
		
		daily_link_performance = {}
		for promoted_link_id in promoted_link_ids:
			path = 'promotedLinks/' + promoted_link_id + '/performanceByDay/'
			
			daily_link_performance[promoted_link_id] = {}
			current_day = start_day
			while current_day < end_day:
				next_day = current_day + timedelta(days=1)
				params = {'from': current_day.date(), 'to': next_day.date()}
				results = self._request(path, params)
				
				metrics = results['overallMetrics']
				if metrics['cost'] + metrics['impressions'] + metrics['clicks'] > 0:
					daily_link_performance[promoted_link_id][current_day] = metrics
				current_day += timedelta(days=1)
		return daily_link_performance
