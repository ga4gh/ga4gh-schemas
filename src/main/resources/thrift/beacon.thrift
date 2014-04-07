namespace * org.ga4gh

struct BeaconPopulation {
  1: optional string name;
  2: optional string referenceVersion;
}

/**
 * The response from the server must either be a “YES”/“NO”, or the count.
 * The server decides with which type it responds. The frequency can be translated to the exists by the relationship of a non-zero result.
 */
union BeaconResponse {
  1: bool exists;
  2: i64 frequency;
}

service Beacon {
  BeaconResponse query(
    1: BeaconPopulation population,
    2: string chromosome,
    3: i64 coordinate,
    4: string allele);
}