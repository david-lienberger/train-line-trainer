<script lang="ts">
	import { onMount } from 'svelte';
	import FlashCardViewer from '../components/FlashCardViewer.svelte';
	import type { NetzplanData } from '../model/netzplan-data-interfaces';

	let netzplanData: NetzplanData | null = null;

	onMount(async () => {
		const response = await fetch('./netzplan-data.json')
			netzplanData = await response.json();
	});
</script>

<div>
	<FlashCardViewer data={netzplanData} />

<!--	{#if netzplanData}
		<div>
			<h1>Origins</h1>
			{#each netzplanData.origins as origin}
				{#each Object.entries(origin) as [stationKey, station]}
					<p>{stationKey}: {station.label}</p>
				{/each}
			{/each}
		</div>
	{:else}
		<p>Loading...</p>
	{/if}-->
</div>
