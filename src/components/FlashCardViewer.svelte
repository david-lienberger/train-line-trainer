<script lang="ts">
	import type { NetzplanData } from '../model/netzplan-data-interfaces';
	import FlashCard from './FlashCard.svelte';

	export let data: NetzplanData | null;

	let currentIndex = 0;
	$: currentLine = data?.general.all_lines[currentIndex];

	$: hasPrevious = data && currentIndex >= 1
	$: hasNext = data && data?.general.all_lines.length - 1 > currentIndex
	const selectNext = () => {
		if (hasNext) {
			currentIndex++;
		}
	}

	const selectPrevious = () => {
		if (hasPrevious) {
			currentIndex--;
		}
	}
</script>

<style lang="scss">
	#flash-cards {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
		margin-top: 15rem;

		#controls {
			display: flex;
			flex-direction: row;
			gap: 1rem;
		}
	}
</style>

<div id="flash-cards">
	{#if data}
		<FlashCard line={currentLine} />
	{/if}

	<div id="controls">
		<button disabled={!hasPrevious} on:click={selectPrevious}>
			Vorherige
		</button>

		<button disabled={!hasNext} on:click={selectNext}>
			Nächste
		</button>
	</div>
</div>
