#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 API for pm25.in
"""
import json
from inspect import signature
from functools import wraps
from urllib.parse import (
    urlencode, unquote, urlparse, parse_qsl
)
from urllib.request import urlopen, Request
import pandas as pd
_default_public_token = '5j1znBVAsnSf5xQyNQyq'
class Base(object):
    """
    Base class for pm25
    """
    _token = None
    def __init__(self, token=None):
        self._token = token or _default_public_token
        assert(self._token)
    def _get(self, uri, params, headers=None):
        params.update({'token': self._token})
        uri += '?' + urlencode(params)
        req = Request(uri, headers)
        response = urlopen(req)
        return json.loads(response.read().decode())
def typeassert(*ty_args, **ty_kwargs):
    """
    param vaild check
    """
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate
class PM25(Base):
    """
        API for pm25.in
    """
    @typeassert(city=str)
    def pm25(self, city, avg=True, stations='yes'):
        """
        1.1 获取一个城市所有监测点的PM2.5数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/pm2_5.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def pm10(self, city, avg=True, stations='yes'):
        """
        1.2 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/pm10.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def co(self, city, avg=True, stations='yes'):
        """
        1.3 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/co.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def no2(self, city, avg=True, stations='yes'):
        """
        1.4 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/no2.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def so2(self, city, avg=True, stations='yes'):
        """
        1.5 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/so2.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def o3(self, city, avg=True, stations='yes'):
        """
        1.6 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/o3.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def aqi_detail(self, city, avg=True, stations='yes'):
        """
        1.7 获取一个城市所有监测点的PM10数据
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/aqi_detail.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(city=str)
    def only_aqi(self, city, avg=True, stations='yes'):
        """
        1.8 获取一个城市所有监测点的AQI数据（不含详情，仅AQI）
        参数
* city：城市名称，必选参数
* avg：是否返回一个城市所有监测点数据均值的标识，可选参数，默认是true，不需要均值时传这个参数并设置为false
* stations：是否只返回一个城市均值的标识，可选参数，默认是yes，不需要监测点信息时传这个参数并设置为no
        """
        uri = 'http://www.pm25.in/api/querys/only_aqi.json'
        params = {'city': city, 'avg': avg, 'stations': stations}
        return self._get(uri, params)
    @typeassert(station_code=str)
    def aqis_by_station(self, station_code):
        """
        1.9 获取一个监测点的AQI数据（含详情）
        参数
* station_code：监测点，必选
        """
        uri = 'http://www.pm25.in/api/querys/aqis_by_station.json'
        params = {'station_code': station_code}
        return self._get(uri, params)
    @typeassert(city=str)
    def station_names(self, city, stations='yes'):
        """
        1.10 获取一个城市的监测点列表
        参数
* city：城市名称，必选参数
        """
        uri = 'http://www.pm25.in/api/querys/station_names.json'
        params = {'city': city, 'stations': stations}
        return self._get(uri, params)
    @typeassert(cities=list)
    def querys(self, cities):
        """
        1.11 获取实施了新《环境空气质量标准》的城市列表，即有PM2.5数据的城市列表
        参数
* city：城市名称，必选参数
        """
        uri = 'http://www.pm25.in/api/querys/querys.json'
        params = {'cities': cities}
        return self._get(uri, params)
    def aqi_rank(self):
        """
        1.12 获取一个城市所有监测点的aqi_rank
        """
        uri = 'http://www.pm25.in/api/querys/aqi_ranking.json'
        params = {}
        return self._get(uri, params)

