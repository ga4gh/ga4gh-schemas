RnaQuantificationMethods
************************

 .. function:: searchFeatureGroups(request)

  :param request: SearchFeatureGroupsRequest: This request maps to the body of 'POST /featuregroups/search'
    as JSON.
  :return type: SearchFeatureGroupsResponse

Gets a list of 'FeatureGroup' matching the search criteria.

'POST /featuregroups/search' must accept JSON version of
'SearchFeatureGroupsRequest' as the post body and will return a JSON
version of 'SearchFeatureGroupsResponse'.

 .. function:: getFeatureGroup(id)

  :param id: string: The ID of the `FeatureGroup`.
  :return type: org.ga4gh.models.FeatureGroup

Gets a `FeatureGroup` by ID.
`GET /featuregroups/{id}` will return a JSON version of `FeatureGroup`.

 .. function:: searchRnaQuantifications(request)

  :param request: SearchRnaQuantificationsRequest: This request maps to the body of 'POST /rnaquantifications/search'
    as JSON.
  :return type: SearchRnaQuantificationsResponse

Gets a list of 'RnaQuantification' matching the search criteria.

'POST /rnaquantifications/search' must accept JSON version of
'SearchRnaQuantificationsRequest' as the post body and will return a JSON
version of 'SearchRnaQuantificationsResponse'.

 .. function:: getRnaQuantification(id)

  :param id: string: The ID of the `RnaQuantification`.
  :return type: org.ga4gh.models.RnaQuantification

Gets a `RnaQuantification` by ID.
`GET /rnaquantifications/{id}` will return a JSON version of `RnaQuantification`.

 .. function:: searchRnaQuantificationSets(request)

  :param request: SearchRnaQuantificationSetsRequest: This request maps to the body of 'POST /rnaquantificationsets/search'
    as JSON.
  :return type: SearchRnaQuantificationSetsResponse

Gets a list of 'RnaQuantificationSet' matching the search criteria.

'POST /rnaquantificationsets/search' must accept JSON version of
'SearchRnaQuantificationSetsRequest' as the post body and will return a JSON
version of 'SearchRnaQuantificationSetsResponse'.

 .. function:: searchExpressionLevels(request)

  :param request: SearchExpressionLevelsRequest: This request maps to the body of 'POST /expressionlevels/search'
    as JSON.
  :return type: SearchExpressionLevelsResponse

Gets a list of 'ExpressionLevel' matching the search criteria.

'POST /expressionlevels/search' must accept JSON version of
'SearchExpressionLevelsRequest' as the post body and will return a JSON
version of 'SearchExpressionLevelsResponse'.

 .. function:: getExpressionLevel(id)

  :param id: string: The ID of the `ExpressionLevel`.
  :return type: org.ga4gh.models.ExpressionLevel

Gets a `ExpressionLevel` by ID.
`GET /expressionlevels/{id}` will return a JSON version of `ExpressionLevel`.

.. proto3:message:: SearchRnaQuantificationSetsRequest

  :field dataset_id:
    The `Dataset` to search.
  :type datasetId: string
  :field page_size:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type page_size: int32
  :field page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type page_token: string

  This request maps to the body of 'POST /rnaquantificationsets/search'
  as JSON.

.. proto3:message:: SearchRnaQuantificationSetsResponse

  :field rna_quantification_sets:
    The list of matching quantification sets.
  :type rna_quantification_sets: repeated RnaQuantificationSet
  :field next_page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type next_page_token: string

  This is the response from 'POST /rnaquantificationsets/search' expressed as JSON.

.. proto3:message:: SearchRnaQuantificationsRequest

  :field rna_quantification_set_id:
    If present, return only Rna Quantifications which belong to this set.
  :type rna_quantification_set_id: string
  :field dataset_id:
    The `Dataset` to search.
  :type datasetId: string
  :field page_size:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type page_size: int32
  :field page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type page_token: string

  This request maps to the body of 'POST /rnaquantifications/search'
  as JSON.

.. proto3:message:: SearchRnaQuantificationsResponse

  :field rna_quantifications:
    The list of matching quantifications.
  :type rna_quantifications: repeated RnaQuantification
  :field next_page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type next_page_token: string

  This is the response from 'POST /rnaquantifications/search' expressed as JSON.

.. proto3:message:: SearchExpressionLevelsRequest

  :field quantification_group_id:
    If present, return only ExpressionLevel records which belong to this group.
  :type feature_group_id: string
  :field rna_quantification_id:
    The rnaQuantification to restrict search to.
  :type rna_quantification_id: string
  :field threshold:
    Only return ExpressionLevel records with expressions exceeding
      this value.  (Defaults to 0.0)
  :type threshold: float
  :field page_size:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type page_size: int32
  :field page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type page_token: string

  This request maps to the body of 'POST /expressionlevels/search'
  as JSON.

.. proto3:message:: SearchExpressionLevelsResponse

  :field expression_levels:
    The list of matching quantifications.
  :type expression_levels: repeated ExpressionLevel
  :field next_page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type next_page_token: string

  This is the response from 'POST /expressionlevels/search' expressed as JSON.

.. proto3:message:: SearchFeatureGroupsRequest

  :field dataset_id:
    The `Dataset` to search.
  :type dataset_id: string
  :field page_size:
    Specifies the maximum number of results to return in a single page.
      If unspecified, a system default will be used.
  :type page_size: int32
  :field page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type page_token: string

  This request maps to the body of 'POST /featuregroups/search'
  as JSON.

.. proto3:message:: SearchFeatureGroupsResponse

  :field feature_groups:
    The list of matching feature groups.
  :type feature_groups: repeated FeatureGroup
  :field next_page_token:
    The continuation token, which is used to page through large result sets.
      To get the next page of results, set this parameter to the value of
      'nextPageToken' from the previous response.
  :type next_page_token: string

  This is the response from 'POST /featuregroups/search' expressed as JSON.

