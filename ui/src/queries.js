import Query from 'app/Query';

export function entitiesQuery(location) {
  const context = {
    highlight: true,
    'filter:schemata': 'Thing',
  }
  return Query.fromLocation('entities', location, context, '')
}


export function collectionContextQuery(context, location, collectionId, name) {
  const path = collectionId ? 'entities': undefined;
  return Query.fromLocation(path, location, context, name);
}



export function collectionSearchQuery(location, collectionId){
  const context = {
    'filter:collection_id': collectionId
  }
  return collectionContextQuery(context, location, collectionId, 'cs')
}

export function tripReportsQuery(location) {
  const context= {'exclude:category': 'casefile'}
  return Query.fromLocation('collections', location, context, 'collections')
}


export function collectionDocumentsQuery(location, collectionId) {
  const context = {
    'filter:collection_id': collectionId,
    'filter:schemata': 'Document',
    'empty:properties.parent': true
  }
  return collectionContextQuery(context, location, collectionId, 'documents')
}

export function datasetsQuery(location) {
  const context = { 'exclude:category': 'casefile' }
  return Query.fromLocation('collections', location, context, 'collections')
    .defaultFacet('countries')
    .defaultFacet('category')
    .defaultFacet('created_at', 'desc')
}
